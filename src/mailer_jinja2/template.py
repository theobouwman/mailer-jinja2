import jinja2 as j


def generate_template(template_name: str, **kwargs) -> str:
    try:
        file = open(template_name)
    except FileNotFoundError:
        raise FileNotFoundError('File: %s not found.' % template_name)

    template = j.Template(file.read())

    return template.render(kwargs)
