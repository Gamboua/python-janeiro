from lxml import etree
import jenkins


root = etree.parse('jenkins-template.xml')

# # Busca por uma tag
builders = root.findall('builders')[0]

hudson = etree.Element("hudson.tasks.Shell")

command = etree.Element("command")
command.text = "echo testando command"

hudson.append(command)
builders.append(hudson)

with open('file.xml', 'w') as f:
    f.write(str(etree.tostring(root, pretty_print=True, encoding="unicode")))

srv = jenkins.Jenkins('http://10.100.0.192:8080')
srv.create_job('Beta', str(etree.tostring(root, pretty_print=True, encoding="unicode")))
