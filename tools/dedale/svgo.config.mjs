// Configuration svgo figée (svgo 4.0.0) pour les schémas de Dédale : on garde les couches nommées,
// même vides, le titre, la description et les métadonnées de licence.
export default {
  multipass: false,
  floatPrecision: 1,
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          cleanupIds: false,
          removeEmptyContainers: false,
          removeHiddenElems: false,
          removeMetadata: false,
          removeDesc: false,
          inlineStyles: false,
          minifyStyles: false,
          collapseGroups: false,
          mergePaths: false,
          removeUnknownsAndDefaults: { keepDataAttrs: true, keepRoleAttr: true, keepAriaAttrs: true },
        },
      },
    },
  ],
};
