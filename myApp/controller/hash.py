import hashlib

mdp='admin'
mdp = hashlib.sha256(mdp.encode())
mdpC=mdp.hexdigest()
print(mdpC)