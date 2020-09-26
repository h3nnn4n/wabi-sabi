const path = require('path');
const webpack = require('webpack');


module.exports = {
  entry: './assets/index.js',
  target: 'web',
  mode: 'development',
  output: {
    path: path.resolve(__dirname, 'web/static'),
    publicPath: "/static/",
    filename: '[name].js',
    chunkFilename: "[id]-[chunkhash].js",
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      'window.$': 'jquery'
    }),
    require('autoprefixer')
  ],
  devServer: {
    port: 8081,
    writeToDisk: true,
  },
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/,
        loader: 'file-loader',
        options: {},
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader',
            options: {
              importLoaders: 1,
            }
          },
          //{
            //loader: 'postcss-loader',
            //options: {
              //postcssOptions: {
                //plugins:[
                  //'autoprefixer'
                //]
              //}
            //}
          //},
          {
            loader: 'sass-loader'
          }
        ]
      }
    ],
  },
  watchOptions: {
    ignored: /node_modules/
  }
};
