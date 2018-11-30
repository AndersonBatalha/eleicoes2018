$('.ui.accordion')
  .accordion('refresh');


$('.barra_lateral').first().sidebar('attach events', '.botao');
$('.botao').removeClass('disabled');