odoo.define('petstore.petstore', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');

var _t = core._t,
    _lt = core._lt,
    QWeb = core.qweb;


var HomePage = Widget.extend({
    start: function (){
        console.log("pet store home page loaded");
    },
});
core.action_registry.add('petstore.homepage', HomePage);
});
