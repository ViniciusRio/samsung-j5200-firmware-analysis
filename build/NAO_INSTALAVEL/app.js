(function () {
  'use strict';
  var buttons = Array.prototype.slice.call(document.querySelectorAll('#tiles button'));
  function columns() {
    return window.matchMedia && window.matchMedia('(max-width: 700px)').matches ? 2 : 3;
  }
  var status = document.getElementById('status');
  function nextIndex(current, key) {
    if (key === 'ArrowRight') return Math.min(current + 1, buttons.length - 1);
    if (key === 'ArrowLeft') return Math.max(current - 1, 0);
    if (key === 'ArrowDown') return Math.min(current + columns(), buttons.length - 1);
    if (key === 'ArrowUp') return Math.max(current - columns(), 0);
    return current;
  }
  function keyName(event) {
    var names = { 37: 'ArrowLeft', 38: 'ArrowUp', 39: 'ArrowRight',
                  40: 'ArrowDown', 27: 'Escape' };
    return event.key || names[event.keyCode] || '';
  }
  document.addEventListener('keydown', function (event) {
    var index = buttons.indexOf(document.activeElement);
    var key = keyName(event);
    if (index < 0) return;
    if (/^Arrow(Left|Right|Up|Down)$/.test(key)) {
      event.preventDefault();
      buttons[nextIndex(index, key)].focus();
    } else if (key === 'Escape') {
      status.textContent = 'Seleção cancelada.';
    }
  });
  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      status.textContent = button.getAttribute('data-title') + ': demonstração local; nenhum comando enviado à TV.';
    });
  });
}());
