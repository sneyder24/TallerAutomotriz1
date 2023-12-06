 
//cambiar de tema
function cambiarTema(tema) {
  const body = document.querySelector('body');
  body.className = `theme-${tema}`;
  localStorage.setItem('tema', tema);
}

const temaGuardado = localStorage.getItem('tema');

if (temaGuardado) {
  cambiarTema(temaGuardado);

  if (temaGuardado === 'dark') {
    document.getElementById('icono-sol').classList.add('d-none');
    document.getElementById('icono-luna').classList.remove('d-none');
  } else {
    document.getElementById('icono-sol').classList.remove('d-none');
    document.getElementById('icono-luna').classList.add('d-none');
  }
}

const temaToggle = document.getElementById('tema-toggle');
temaToggle.addEventListener('click', () => {
  const body = document.querySelector('body');
  if (body.classList.contains('theme-light')) {
    cambiarTema('dark');
    document.getElementById('icono-sol').classList.add('d-none');
    document.getElementById('icono-luna').classList.remove('d-none');
  } else {
    cambiarTema('light');
    document.getElementById('icono-sol').classList.remove('d-none');
    document.getElementById('icono-luna').classList.add('d-none');
  }
});


