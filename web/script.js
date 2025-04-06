function enterApp(){
  window.location.href = "main.html";
}

function generateTemplate(){
  const projectName = document.getElementById('projectName').value;
  const language = document.getElementById('language').value;
  eel.generate_template(language, projectName)(function(template){
    document.getElementById('templateOutput').textContent = template;
  });
}