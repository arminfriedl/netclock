const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const path = require('path');

module.exports = {
    entry: {
        netclock: './js/netclock.js',

        countdown_create: './countdown/templates/countdown/create.js',
        countdown_view: './countdown/templates/countdown/view.js',
        countdown_created: './countdown/templates/countdown/created.js',

        worldclock_create: './worldclock/templates/worldclock/create.js'
    },
    plugins: [
        new CleanWebpackPlugin()
    ],
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'static', 'dist')
    },
    module: {
        rules: [{
            test: /\.s[ac]ss$/i,
            use: [
                // Creates `style` nodes from JS strings
                'style-loader',
                // Translates CSS into CommonJS
                'css-loader',
                // Compiles Sass to CSS
                'sass-loader',
            ]
        }]
    }
};
