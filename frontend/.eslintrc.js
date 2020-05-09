module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/standard',
    'eslint:recommended',
    'plugin:vue/recommended'
  ],
  parserOptions: {
    parser: 'babel-eslint'
  },
  rules: {
    'no-console': process.env.VUE_APP_ENVIRONMENT === 'production' ? 'error' : 'off',
    'no-debugger': process.env.VUE_APP_ENVIRONMENT === 'production' ? 'error' : 'off'
  }
}
