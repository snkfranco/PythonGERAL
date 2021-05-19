import subprocess

#current_machine_id está recebendo o get uuid da máquina
current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

#current_machine_bios está recebendo o get serialnumber da bios
current_machine_bios = str(subprocess.check_output('wmic bios get serialnumber'), 'utf-8').split('\n')[1].strip()

print(current_machine_id)
print(current_machine_bios)
print('by: Matheus Franco')

#Aqui voce pode criar ifs fazendo referencia a algum usuário. 
#Poderia ser requisitado que o usuário roda-se esse programa primeiramente em seu computador
#afim de que fosse retornado XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX do UUID
#e também um valor XXXXXXXXXXXXXXX da Bios
#após fazer isso, poderia ser declarado no main uma variável onde( POR EXEMPLO ):

# x = 'USER_UUID'
# current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()

#if x == current_machine_id:
#   ...
