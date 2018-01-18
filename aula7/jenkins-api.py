import jenkins

srv = jenkins.Jenkins('http://10.100.0.192:8080')

# Pegar versao
print(srv.get_version())

# Criar job em branco
# print(srv.create_job(
#     'Python-Job',
#     jenkins.EMPTY_CONFIG_XML
# ))

# Executar Job
srv.build_job('Python-Job')

# Listar todos os jobs
for u in srv.get_jobs():
    print(u['fullname'])

# Mostrar um unico job
print(srv.get_job_info('Python-Job'))

