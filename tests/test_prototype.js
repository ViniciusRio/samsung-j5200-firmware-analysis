'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');

const buttons = Array.from({ length: 5 }, (_, index) => ({
  index,
  handlers: {},
  focus() { document.activeElement = this; },
  addEventListener(type, callback) { this.handlers[type] = callback; },
  getAttribute() { return ['TV ao vivo', 'HDMI 1', 'HDMI 2', 'Aplicativos', 'Configurações'][index]; }
}));
const status = { textContent: '' };
const document = {
  activeElement: buttons[0],
  handlers: {},
  querySelectorAll() { return buttons; },
  getElementById() { return status; },
  addEventListener(type, callback) { this.handlers[type] = callback; }
};
const window = { narrow: false, matchMedia() { return { matches: this.narrow }; } };
vm.runInNewContext(fs.readFileSync('src/prototype/app.js', 'utf8'), { document, window });
function key(value) { document.handlers.keydown({ key: value, preventDefault() {} }); }
key('ArrowRight');
assert.equal(document.activeElement.index, 1);
key('ArrowDown');
assert.equal(document.activeElement.index, 4);
key('ArrowDown');
assert.equal(document.activeElement.index, 4);
key('ArrowLeft');
assert.equal(document.activeElement.index, 3);
buttons[3].handlers.click();
assert.match(status.textContent, /demonstração local/);
key('Escape');
assert.equal(status.textContent, 'Seleção cancelada.');
window.narrow = true;
document.activeElement = buttons[0];
document.handlers.keydown({ keyCode: 40, preventDefault() {} });
assert.equal(document.activeElement.index, 2);
console.log('Navegação do protótipo: OK');
