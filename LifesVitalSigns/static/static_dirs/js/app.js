var app = new Vue({ 
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        message: 'Hello Vue!'
    },
    methods: {
        graph: function (message) {
            switch (message) {
                case 'CO2':
                    break;
                case 'GlobalTemperature':
                    break;
                case 'SeaLevel':
                    break;
                case 'ArcticIce':
                    break;
                case 'AntarcticIce':
                    break;
                case 'GreenlandIce':
                    break;
            }
        }
    }
});
