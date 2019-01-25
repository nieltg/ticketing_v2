const path = require("path")

const HtmlWebpackPlugin = require("html-webpack-plugin")

const distDir = path.resolve(__dirname, "dist")

const config = {
  mode: "development",
  entry: "./src/index.tsx",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node-modules/
      }
    ]
  },
  output: {
    filename: "static/webpack/[name]-[hash].js",
    path: distDir
  },
  devServer: {
    contentBase: distDir,
    compress: true,
    port: 9000
  },
  plugins: [new HtmlWebpackPlugin()]
}

module.exports = (_env, argv) => {
  if (argv.mode === "development") {
    config.devtool = "inline-source-map"
  }

  return config
}
