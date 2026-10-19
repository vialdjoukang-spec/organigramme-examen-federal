#!/usr/bin/env python3
"""Patch 0098 : externaliser les déclarations globales sans modifier leur corps.

Rejeu : APP_FILE=app_v2.html python3 tools/patches/0098-externaliser-fonctions.py
Chaque déclaration doit correspondre à l'ancrage unique et à son SHA-256 d'origine.
"""
import hashlib
import os
from pathlib import Path
import sys

MANIFEST = (
    ('monday', 118, 'a6f33bc4a58e5542e66e5a09515cb4c0019090dde3cf5bda56c0dafbf0c8af9b'),
    ('uid', 144, '5862b3a936c799011c051dce08b7aaf30fe090fb7aeee14e1f0c9097d5688721'),
    ('lsSet', 285, '38f89400ab5b519127ae583d697e9179dfe39cb30df71f497ad965314c1dabae'),
    ('bakKeys', 195, 'b1bb29e0c415c036810be4fef29a13011392846af0714ff0c5c328393d807265'),
    ('bakDate', 160, 'a79ea3f2f1e6c46f6f8330c424f9fbde9cd4a8bf431b0bb0688782e6840f31e2'),
    ('bakMsg', 116, '59ab0d7c6e6f01af4eb8609599c2797e6a1af60719935eb115b7cd2982b3b8b6'),
    ('bakShow', 1110, '20e7dd9a678b02849cd1a4b03ca8e4c98228c9e11dd641ace0af3f173a0f90be'),
    ('bakSum', 370, '677131f1f1f3178119edd95f9c5b3363288cad78eb4578b980331254a49ed555'),
    ('bakExport', 709, '8e7bed33c332150aec78c569879c1a7e90495e453bb7ea3113dfd4a16f51183f'),
    ('bakCheck', 828, '4693c8f7c5726787ebb7b7fbe9ebd4451f738a1b6ec92163d0302a929336c194'),
    ('bakMigrate', 38, 'b6f1ef24a46bc7e05ddec312aff5407e55698767de03864f5cf5bd190ed0764b'),
    ('bakRead', 1035, '0328dfda42aa677297e328f9d23db63219a68cd911f50e3bcc74488b94adc2ac'),
    ('bakApply', 578, 'cefc87b1aa8fd23c620f59f364c0a6f3cf3779efe4f3c2a0052023e8fa9c6ab3'),
    ('svCanon', 82, '8d07af2a8dfad15b9ef14645b9a9e2a04a954f5f315e5590daed0c5e487db125'),
    ('svSum', 188, '85b15a3baa775445a45276563cf16d5b4daef9d17e2e445add6fd56949be4888'),
    ('svOk', 140, '9b0a2cc98b313d2f8a0127c125cfb8c71c898dfea6ed29e6abb2bc3bef90e009'),
    ('svOpen', 378, 'f4a7e64eb95f91c772a621612dd8ba8d4b2d1a23015d2e42cdecbce9b2889c86'),
    ('svTx', 229, '55da0e03c39796d88548fe1aa2be3ab41e9a15e5ae1b83089360c95c34c133f9'),
    ('svRec', 109, '5aa9d7f1710f2e5954d45427b2512e78a593c69acaaf60bf7461eece87f56545'),
    ('svTouch', 84, '2aeb8ca3b3b89555212ee516f60ca9a513880487abe992b5598dde28bf82b097'),
    ('svHm', 88, 'd2ded7ad4ed6dd2280136541b0fca6f379cfbe06230f7aed38bae13cd10922c9'),
    ('svStat', 357, 'a6cb9292a57fe169e982c77db8db23ccb13221fea8c88ee08c13f0056c639ceb'),
    ('svFileBtn', 279, '1fd202a7cf483cc24cffbdc50d9e42a7b0a8738e680d2ee593a17dbdd996faad'),
    ('svFileWrite', 752, '193f19a10ee675b314d393f6037c620ae633ffb8f5b303eea8b85aa31cd4d1c9'),
    ('svWrite', 328, '72ad76cff54e7c582d6fc4ea31ff31f459a949529724f227e052d98e374003cf'),
    ('local', 173, '18ce57f7dbbfe8ffaf04b99b72165e24f05830afcb9d88ca3a2592dab8475554'),
    ('ckDone', 104, '267f6be6f4442774889e8f9aab4a0792df67f70c87e06569e8b93460b7017fd7'),
    ('hl', 175, '953b2395b0b09bbeafdbd48cad4880032d75f445e9c1ba38c9d75e9c8575e7f8'),
    ('renderList', 1072, '5c574f240b6988d95b2e1c1ac3dfdff2f2850cbce1688e465a3f0d7e45744494'),
    ('days', 193, '7ab5b095b528a6ebaa5a9d3e61955e6eef853047303441958506dbd2bdf48384'),
    ('renderGrid', 1867, '961ef75d38ea7be90ceae0e570979f6046be6213348cfbd3084a179a956c0333'),
    ('minuteAt', 153, '31ae1994ba8df1bc28f3ea45ca0cfd1cfbad0ccec6720e4b85e35ff37443d475'),
    ('addAt', 269, '81764794a66d48d8978169b83cab0d53412aec2aea3aaf906c570e9918a52ac5'),
    ('calSay', 80, '070e7c69310a5c4443c8e24a1c13f1fd6b519e696b356585b3c97aceb09d7a33'),
    ('calMin', 187, '5faad2f3216406fb1a1c78f69ec3a50a5a3d8d3ffc2b4b66fd5b15a6f9e0147a'),
    ('calLab', 123, '05965c423f86f1faeffc85f0bd49f1571c516803dcf7a47de7c3552f9b9e42e4'),
    ('lev', 206, '93eb5054f243c15e7d1000cd52dd58a802d6a3eb15a85d58a7db77e16c6a0abb'),
    ('fzScore', 550, 'ad88dc5c85f343d4b098802ce477b88668fe4bc3e3471984dab7cddb07481765'),
    ('fzNotScore', 225, 'c72dcbfd57589f160d5491047e1bfa075d82981172c529b5fd2a4efd19181684'),
    ('fz', 324, 'a1042d419bf8f45daed864f3658cc80e39b3f3caf2ee5a053abd889c3ec565ff'),
    ('cqRender', 731, '0a191b9c3228d2992833a6872bb5e9fbda66681864915d5c98e881c5fc041b21'),
    ('cqOpen', 599, '82cee6d752e17c4e8656c5f250551dd99aff0c536490694dabd8bb5e74f40ad1'),
    ('qpDur', 204, '724f2848884d5b898b90beeabc6cbd512928c11c35c498f370bf42834c868fb3'),
    ('qpOpen', 748, '25d4491b6d70717a092ed9fcf9431c591154c0367cf312111f783c72af0fa01d'),
    ('qpClose', 52, '59053f73bcc6846b93508d1f8e15ce924099fc46aa8fadcb61db4540ae622cc1'),
    ('qpRender', 304, '566af0fc3e5d87a95014cd5e16bf1b0516037c4c85407a1a9f21b24ee756fd1c'),
    ('qpCreate', 647, 'd34872ecc57f29bb965055c2fc1253616c1688d4cc6279f75f09c13697a80e2f'),
    ('calSupp', 66, '9d9c81e8ac420bec0adfda2459b20fd957d911867bcb81a9d1e4cd9ac24a395d'),
    ('calRange', 114, '42eee28d7b57547a5cb6787787e74ce3e6fa5148ec2f0146cf30ad4bd4323586'),
    ('openEdit', 530, '3edb92cb85cc1bb377e0f8ace1d91908236ee1819d9937bf17de23c402fd2188'),
    ('agg', 901, 'f91bffc0c79d1d0b9f1e417b6ec7a25ab280e5c47648521f5c85b2966f533cda'),
    ('renderKpis', 448, 'd7e9781d5dbff519b5ef483c9644c72e46517a7cad153bacc89d2dbc99789091'),
    ('ring', 563, 'c6277b664c85b74e24812575b90b57d17c2b7228d79ff6ee31ddebe237e1778a'),
    ('renderVit', 3316, '4191166963f91c3a6a0f416a8d32467f46c16b75a733b94b96b53dda6ffec531'),
    ('renderCalc', 1685, '76aee123b35105c9364e79c1c6eceac23c7c55249480b5ab989138e3a5cdce13'),
    ('exiMig', 224, '9a3ab4fd87f22a7d8ffdfbd52abd45f2632c7d631422c290dd857d1bee54f36b'),
    ('exiBanner', 1300, '3109cbe1debc81f7a791f78942d6086ada652b0bc9d8852f4d47c12627df6ab0'),
    ('renderExi', 1105, 'b4e7782aadb1c110e1b379d7c0f8a5a9e024f49a3bede338aa9b7290b96b2de2'),
    ('applyDisp', 319, '3c268201bd235f43d159ff181b718e5010b43cc2b7e7016ae25794a0d1491325'),
    ('memMd', 72, '7043665c174a8ef7e92d93f8004f0f7235bcb5c6618b00c43f5c53acd55a5a7a'),
    ('memDoi', 116, '1eef42db52bb736d0a5ee367da7694278d67e804519e3d8a9eecff7771943144'),
    ('memMed', 252, 'a3869f4a629c5d9b8bc857d18fd05fc3855d1bdde19623f56b6d766ab4f534e3'),
    ('memTip', 1146, 'f706aae3711df86ad9e803baea37fade0d5f94e3256cdc4ec0a8a51e9a913874'),
    ('memCard', 885, '27c33df6e1f907ad88e423578bf6d775907c6fff9092e0048a66ea25a95d6aae'),
    ('memEv', 277, '61952a0522bf41bfbf9192881c5aea1c264e111e4106e96e2bb972d0097b1723'),
    ('memI', 203, 'fd930f40692d46a049f28f51b5c3380fceb6b8804d6c4304541a112287702e31'),
    ('memOpt', 460, 'f7f44dcd9c6b5f0619d27b968cd3b498a5ee31b7d91b29ad5072857ab0268e1f'),
    ('memW', 165, '376f5cb344b399871db679c3b966f1821df3949d1256e8cda3178132038bf715'),
    ('memCons', 759, '8d288e01eb46f333519612ac49fb4f2f6b88e82ebf4a268a947875d0ec2e6d6b'),
    ('M', 61, '66ba7684e63039304f651f4ac74e9826d1987649ce621840f20e784b52c55a1c'),
    ('ints', 92, '56eb3cab7dfc4cffc9e4a27ed667d78da54ed85da172918ff92b838430674905'),
    ('memoState', 788, '1822107f25629a6bc80cefd3e98517a4bdd29a3a498fe590bef5fdaf874ffe74'),
    ('renderMemo', 3101, '7a7b82477360ea3aedda28c3b79f432c771d2abcbff0fdc8b5812ad3c8509414'),
    ('renderCSPlan', 303, '27f5558cd12d0b852b970a817f7d3d23a48a1e5ed761cdb47b7bb44df31bc2db'),
    ('renderPicks', 146, '520c68e90ca12842d940348776d0fee157b4899506ddddfb96ac1489200aa435'),
    ('scenario', 5000, 'a4e5d1809bd9d08b53995e45cf4091bdcc2be53abce1136d2fe7166556cbee3d'),
    ('selOut', 198, '18550f1eff9a077fe8190f33be56b482e661c1f312d1ec3147aaeb9f0dddf6e8'),
    ('renderCSLog', 1742, '38a197d5da7a1b3e80dd45946f28c2fd21239b54c0642e520404e79f107d3119'),
    ('renderAtt', 434, 'a34c5ad408aadb67fa69b8af2c0cc4a63741716c0baee6a9b3e33ce0397544ef'),
    ('nGet', 63, '6ccd6fcb132bd52865c2bb7952214ddf8b8dd58d8d85bcf0e6b5c4e42bd39ada'),
    ('notList', 440, 'd4b1b02ba40d53fed79499774b4904977c000c6e5ff0f59c1ebc7f92dee320a3'),
    ('nStat', 230, '456f1698822bf110524ce836f739952900c2586e7b3faf467720659d5e82044b'),
    ('nSave', 240, 'f10d6d5553b6b3519f0020475638084ffdd90ed66f938d3d69b73db5eecfa621'),
    ('nRow', 835, 'f4c22d929a20800a341343e31802a2e1787c8dde46766a608f2f3c33fc65fc34'),
    ('nBlock', 1747, '19cc790138a16059b3fece4ede794c8735aa661f676e495ead756aae76731b9a'),
    ('nWire', 1346, '44f76b7f4686b544515b9edc880da5cd917b4babddbd6480f5e4adb5646cc00a'),
    ('renderNotSoft', 732, '928d3ab6984bed48b5fe346308468cc735bd3c4c0126ecb4bf12acd6d0e33d0c'),
    ('nGlobal', 302, 'b5bf75eb72ada9268b5336ebe816520737fd4f4be0727f10ecef145524a71296'),
    ('renderNotStats', 3213, '23987ce36c84a8c089283c16f470db90ab44feb558001c477dc9c3c5b5064acb'),
    ('renderNList', 529, 'a9c65cf0bf518248bc628dc0e76a87728af7f7a6b78a3eee742d94e336290e18'),
    ('stLoad', 431, '7464aca6a67b4cfe1b054d84186ad77f328b7b0026103ff1ee4b84561a4b9270'),
    ('stMount', 724, '653222ecb5c6c28fcfb40fdee24e4e2c25c862ecd2c8a9fc91f2e27bca580667'),
    ('stOpen', 641, 'c6a35407273f34dbd3eb8ef297be8ba710a96dcc9ddf0a3389e91db7e08f5c9d'),
    ('stAv', 97, 'fd5aff66285619bf5954d4de0d0d601a59e178103402b2a201628053e605fa63'),
    ('stSrc', 90, 'cecb59b2e88dbdfbd2b4955a6847c664e97a13014327657702f6606d19fe93fd'),
    ('stSrcC', 332, '034edb2224e094ba8cbe68c03d0aa91b0978a9b0a58f50372afb515a91f0605a'),
    ('stUl', 126, '8583fc91a0717fcdd216e51bdd923102f09e38f8a112827bec2d8cf8e8d4bd1f'),
    ('stHtml', 3003, 'fb4d8af84df4c214bbeb05c2195a6faf33141bc5ea6d9b23908bbd4cc2c08329'),
    ('renderNot', 277, '3f128859c5ea6135db1496a7b7e4ffa5c8a098000add69e62eba9f1409487e60'),
    ('gK', 44, '90be082e56604ba3299062a78d516e9b0e7c2acc8afcb4c68aca12e28ac8bef1'),
    ('gFig', 345, '1f9c0812ca67d6f0f7f23866eb9a297fc1ced35d4b528afcc696fcf14fc6089e'),
    ('gGroup', 398, 'f2322ed698a3f844e53abc6445362146a3eb4389eea0d253c4c614b458b2e9b8'),
    ('exFmt', 1375, '31369a58b8ae5d24debc3cf3c246cc59866d18222ca1beedf751775470c319d3'),
    ('gGo', 523, '2a3cf4a4f12bedfd8253768952e1ad23d6706de5920b5b040b88a511c275d031'),
    ('renderGes', 2176, '99f10b091368796abdbbb1cdcc392c7122246b98c7f3036804be0a9318e85209'),
    ('parseRes', 359, '65a9eb39efca27e869a24b73670e22cbb57ea9f1f645e108fd1d24ffc8b90c7a'),
    ('pvRankText', 324, '4acf970544ce91cb01bbd791817e3c5e9152c7928fb61ffe0a72bdad545e00ca'),
    ('pvOf', 74, 'cf36cd3429b5b072b4a664363eac326c986854a100e93e9e0b8e4a9f043867b8'),
    ('pvFmt', 158, 'a8474beaf9667f20d755e1434f0187db669513c0693498900508eaf2922fc3ea'),
    ('pvSpan', 174, '4aee3cee818568291ea3eddf8c5ee466423f837074c1e8bb1c5133fff527e2ac'),
    ('pvLine', 231, '7c9e3367fe9167606dba3e3923bf741ae6826d3b622219782493272046366658'),
    ('ckGlo', 92, '7e6aa8267d5dce63509ec3ef10cf2aecbb362a365a03ecaaea16728b8e54aebd'),
    ('monoId', 147, 'c20347f8ffd1f05b9b25b712ba548b229b01c55bd4500169652f8d63a67a9b94'),
    ('monoGet', 336, '1d1f4e92860e0d0b51cf3a5186a2a5f247e0f43fabf462cce7adbce1416941dc'),
    ('tipFor', 2018, 'eea6e9785a397eeffd508d19f07fe0806cb168864d2b8caafa3dc9929d70e2db'),
    ('showTip', 2474, 'a7fc684da0c32cbc38806097a472af87b354c64bdadf15400e5178bceaf7b6f0'),
    ('hideTip', 367, 'ad83b7d2050ec4039faa6b72512f0f4a8417007a05a9650831669190ee19663b'),
    ('tipToggle', 144, 'cd8bef1b0f3585c8a1b5e07a92840dde31c9416b6106b01c52d2274cc87b9a51'),
    ('blkFit1', 469, 'bfae2577c21e63055e9fce4a31522ebcd5e852c81eb1c7ffea70d7a78b68e1b8'),
    ('blkFit', 75, '75ef1b12aa126bb6e777ca995e59f5a79ac5c1fb47f4edac3048a4d333869401'),
    ('ckW', 39, 'b03cea1d043e6cd991bf240ab6824e5f2dcecbc6dba7d8276a23345282b7a7f3'),
    ('ckFold', 164, '3798d6daad96b90badd3be86d44217d3787ecc15e221d8f7ccad08a9afd45404'),
    ('ckData', 156, 'c54fe8f8bb0a359406b17fdeaacfbddb76f34c1fc7dbb04e1f283fc48ac36167'),
    ('ckDate', 111, '6bcf22aa1dd3416091504beac013411a7ae61d9bf4273fd8262257538c03758a'),
    ('ckRe', 64, '5a9850e9fa66657133ab1feaa19b059d6271de514cd37334ca2aaf670b29998b'),
    ('ckP', 82, '7d091649a8a733d8ec0830808f7e10eca69199e8b8812e891f40d20a2be67a88'),
    ('gloIndex', 887, 'e4c3f39ece29fb21c79c4ebff38b1eec744057f030695144ae4e1b92eab06da4'),
    ('gloSl', 103, '9d7bcb97ec567dfa46c382a23c4cdf9485c3089b9234c1e41cc05b075ec5eab8'),
    ('gloE', 157, '2f1d2092eedc6d2e20f9a248fcd7cdb7a8e7da5e32c12ba0a75dd9999218c42f'),
    ('gloMeta', 132, 'dc7ed91bf3e94b6a89737a5c61f9b0c122fb65e2e87e3607ea9a50414d6343c7'),
    ('gloShort', 182, 'b2c31499c8849b436adbfcfdd0266eb6a0c2ab056a913259e372a26a7a87f9d8'),
    ('ckNeed', 516, '15d8f4c72ae4422a75ecd784ce6c0370670b3ffb1ef9b67139a6df980d5d1791'),
    ('gloLink', 1838, '0639d2b5db03c389519d6fad18057e7861a978222d627102da2f598cfc0c3121'),
    ('gloSched', 69, '6b07b84f008a73c406b4280fc9988e50d9d5dcd2f1e6579d8cc6dd0f0473cfd9'),
    ('gloRun', 481, 'a626ae5b3e1e9fa2345971e19a869e9a49780049dbae96a0a16d4e329ca9f68b'),
    ('gloStart', 211, '5b22544181b5350525bce394a17ecf1d4b0103aa7831a67aff435469044362ca'),
    ('ckL', 138, 'a0f0446d733e9c120ad00bbc350d8399614e1e09cf708afc3f3e7430a88a87bb'),
    ('ncVue', 38, '42a9b57f8e5b91fa920babfdca183d4e95e42b64278ba1180c8b3d0d704b3dfe'),
    ('ckLab', 134, '18e31ce0e511d11cb7122b555c9a18e52bdb6704174d6ee750dc04aa42b3550d'),
    ('ckLnk', 151, 'aecb5fc16f3b9b3019f9038629ad469d0f12b5f5d7d9218e319a8c0c2734b342'),
    ('ckGes', 283, 'f439c09c1f13d2e1c52b84393ef24420727308ba007ea48cf75789aba8741f76'),
    ('gLoc', 238, 'd6177b1caaa043c14cde4e19d2841b63a2137ca99c8c5bf1233a5367bb266537'),
    ('ckArr', 59, '18aea37d8c6469386aba82bc5da8bbdc96cfb9d4c763bc1ad877ac6ad14c53e4'),
    ('modLab', 90, 'af7b08fa49e6175a9f61d603b7df4d0a9c84b6ba71f15009ca328070bd5bcf6a'),
    ('ckSrc', 357, '0d0bcfc2735e9f4194c8da03ce8774908084582e5e2caade560c0ece5064fdbc'),
    ('ckFoot', 222, 'ad8851c5cc3a76628e6f35946dea2df44903c4637490d5c127d5c74a70239e68'),
    ('ckJ', 60, '1bac4e17cedefe5738b446e6525816b3445125d0dabc677d3e3a6bc4487a668c'),
    ('ckList', 126, '4b6ae0bb8cb9c1aab8bb02ce00c096c9ad7cddfe6dc9f1e94d350dfd93ff474a'),
    ('ckLinks', 119, '3b460edd3aa5f6d6704653b3f5b45961b36fbb63e192d8ef3b011a1ec61a485d'),
    ('ckDose', 432, '4e2054a1c364dd739eec1c43851dc95c4d82401ec65dd34d4d5aff954c0a384d'),
    ('ckWait', 80, '9d0c0ec1483980554f44dd5195e3f095f2a8a735a65b7dd7f910bc5c73952927'),
    ('ckTip', 7037, '015819b354311ac703ac8c04acd8a09991ec42d8a70b886381d01f7e82a88416'),
    ('ckSvg', 592, 'a6f453391c6c79733eee8f251a6fd06592171a6aae7eed31241205f572b5f076'),
    ('ckEtats', 105, '11d323c4d152a30fbbfd005ff0b110fb7cd4ffb708a8e4bc474a39205aac4590'),
    ('ckEtat', 484, '8cbf1805851c31a7d283b7f4493f5dc0edb589acbef8fbd3e95864a06e63d788'),
    ('ckApply', 480, 'ace034b91f7cdb355ed81fcde27a5086fe0a0213fd9041ff6020d37cbb37f631'),
    ('ckFig', 1978, '0b2f08768646748403bc676ca27ca4c479c9f9ad664ebe701be2211a8fe8f796'),
    ('ckNum', 563, '06c34d41a843189149fc769ebd777904a53eaaea10d5d99a223d5157ae31ca5f'),
    ('ckBulle', 458, 'af9091950c66905b38a09300d93311f4c3d1cdf85fb423bcb7eff1a274c895a5'),
    ('ckBulleX', 80, '9a97e5ede2e4436d48b38c0988c75f0b1408bfae8492ab3359b5e84714969aee'),
    ('ckTour', 197, '8ff6d3f5dfc41474387cc3311bcad7b03b22f850c6b2fca19c86ac6e82580244'),
    ('tipGo', 132, '06509875ec752f6d51273985895ac54ab85be6a183a394d38f7d02795fc032a1'),
    ('tipNav', 1068, '86901df26237965b4a615a2254e73db7ff9c646842f08e5467a9adaca7bf4e11'),
    ('tipCk', 528, '49323d72cc50b20d69a3d91625eb1be5b7bd8eaded9140af3472d86bc2595250'),
    ('renderAll', 267, '63a043d19f6fc95b8af33bae5b75a1db382cb654f02f52f8e5a6cb87d502ad13'),
)
APP_ORIGINAL_SHA256 = "9de6a782af9cd1ab64a3e7658969b93074e9367d1a1f4a3cff294cf3ac7b29ef"
SCRIPT_ANCHOR = '<script>\nconst SSP='
SCRIPT_INSERT = '<script src="assets/config/fonctions.js"></script>\n'
ASSET_REL = 'assets/config/fonctions.js'
SPACED_LINES = ('ckRe', 'ckP', 'gloShort', 'ckEtats', 'ckEtat', 'ckTour')


def sha(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def marker(name):
    return '/* SSP-FONCTION:' + name + ' */'


def extract(original):
    if original.count(SCRIPT_ANCHOR) != 1:
        raise ValueError('Ancrage de script principal absent ou répété')
    if SCRIPT_INSERT in original:
        raise ValueError('Le chargement des fonctions existe déjà')
    matches = []
    for name, width, expected in MANIFEST:
        anchor = 'function ' + name + '('
        if original.count(anchor) != 1:
            raise ValueError(f'Ancrage absent ou répété : {name}')
        start = original.index(anchor)
        body = original[start:start + width]
        if sha(body) != expected:
            raise ValueError(f'Corps modifié ou ancrage déplacé : {name}')
        matches.append((start, start + width, name, body))
    matches.sort()
    script_start = original.index(SCRIPT_ANCHOR) + len('<script>\n')
    script_end = original.index('</script>', script_start)
    if any(start < script_start or end > script_end for start, end, _, _ in matches):
        raise ValueError('Une déclaration sort du script principal')
    if any(a[1] > b[0] for a, b in zip(matches, matches[1:])):
        raise ValueError('Déclarations imbriquées ou chevauchantes')
    chunks = []
    pos = 0
    for start, end, name, body in matches:
        chunks.extend((original[pos:start], marker(name)))
        pos = end
    chunks.append(original[pos:])
    app = ''.join(chunks).replace(SCRIPT_ANCHOR, SCRIPT_INSERT + SCRIPT_ANCHOR, 1)
    asset = ''.join(body + '\n' for _, _, _, body in matches)
    # Six espaces hérités sur des lignes vides restent reconstructibles sans
    # introduire d'espaces terminaux dans le diff de la nouvelle app.
    for name in SPACED_LINES:
        old = marker(name) + '\n \n'
        if app.count(old) != 1:
            raise ValueError(f'Ligne espacée attendue absente : {name}')
        app = app.replace(old, marker(name) + '\n\n', 1)
    restored = app.replace(SCRIPT_INSERT, '', 1)
    for name in SPACED_LINES:
        restored = restored.replace(marker(name) + '\n\n', marker(name) + '\n \n', 1)
    for _, _, name, body in matches:
        if restored.count(marker(name)) != 1:
            raise ValueError(f'Marqueur ambigu : {name}')
        restored = restored.replace(marker(name), body, 1)
    if restored != original:
        raise ValueError('Reconstruction non identique à la source')
    return app, asset


def main():
    p = os.environ.get('APP_FILE') or sys.exit('Indiquez APP_FILE (copie de travail).')
    if p.endswith('orig/app.html'):
        sys.exit('Interdit : orig/app.html')
    app_path = Path(p)
    asset_path = Path(os.environ.get('ASSET_FILE', app_path.parent / ASSET_REL))
    original = app_path.read_text(encoding='utf-8')
    app, asset = extract(original)
    if asset_path.exists() and asset_path.read_text(encoding='utf-8') != asset:
        sys.exit(f'Asset existant différent : {asset_path}')
    asset_path.parent.mkdir(parents=True, exist_ok=True)
    asset_path.write_text(asset, encoding='utf-8')
    app_path.write_text(app, encoding='utf-8')
    print(f'{len(MANIFEST)} fonctions extraites ; {len(original.encode()) - len(app.encode())} octets économisés dans app_v2.html')
    print(f'original SHA-256 {sha(original)} ; reconstruit identique')


if __name__ == '__main__':
    main()
