import eel

eel.init('web')

@eel.expose
def generate_template(language, project_name):
    templates = {
        "html": f"<!DOCTYPE html>\n<html>\n<head>\n\t<title>{project_name}</title>\n</head>\n<body>\n\n</body>\n</html>",
        "python": f"#!/usr/bin/env python\n\n\"\"\"{project_name} project\"\"\"\n\ndef main():\n    pass\n\nif __name__ == '__main__':\n    main()",
        "javascript": f"// {project_name} script\n\nfunction main() {{\n    // code here\n}}\n\nmain();"
    }
    return templates.get(language.lower(), "Шаблон не найден.")

eel.start('initial.html', size=(800,600))