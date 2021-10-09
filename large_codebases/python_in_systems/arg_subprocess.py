import subprocess
import random

p = subprocess.Popen(['emoj', 'dog'], stdout=subprocess.PIPE)

output, err = p.communicate()
p_status = p.wait()

emoji = output.decode('utf-8').split(' ')
print(random.choice(emoji))