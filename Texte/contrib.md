## Créer la clef SSH
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

## Déposer la clef SSH sur github (id_rsa.pub)

## Récupérer le dépot

git clone ...(méthode ssh)

## Paramétrer git

git config user.name "..."
git config user.email "..."

## Gérer les modification
git status
git add <nom-fichier>
git commit -m "le message"

## Synchroniser avec le dépot distant
git push
git pull