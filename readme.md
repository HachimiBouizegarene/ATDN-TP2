
# Rapport TP 2 ATDN2 Bouizegarene Hachimi

### Partie 1 :
\- *"Expliquez le principe de l'optimisation bayésienne." :*

**Réponse :** L'optimisation bayésienne découle du théorème de Bayes. L'objectif de cette méthode est de maximiser ou de minimiser une fonction inconnue f(), c'est-à-dire trouver x qui maximise ou minimise f().
Le principe est le suivant :
- Modéliser f(x) avec un processus gaussien.
- Choisir le prochain point x à tester à l'aide d'une fonction d'acquisition.
-  Mettre à jour le modèle en intégrant le nouveau point f(x). C'est justement grâce au théorème de Bayes que l'on met à jour cette estimation.

\- *"Décrivez comment elle permet de gérer les fonctions coûteuses à évaluer. " :*

On utilise l'optimisation bayésienne si f() est coûteuse à évaluer. On va chercher à choisir intelligemment les x à tester afin d'en essayer le moins possible tout en trouvant la réponse le plus rapidement possible.

\- *"définissez et expliquez les processus gaussiens." :*

**Réponse :** un processus gaussien est une distribution sur des fonctions. Il donne une estimation probabiliste de f(x) en chaque point x, sous forme d'une moyenne μ(x) et d'une incertitude σ(x) (variance).

\- *"Pourquoi sont-ils utilisés pour modéliser la fonction objective ?" :*

**Réponse :** L'optimisation bayésienne a besoin de certains éléments pour fonctionner de manière efficace. Elle choisit les prochains points à tester en fonction de l’incertitude, par exemple si une zone est incertaine, il est préférable d’y tester plus de points.
-> Un processus gaussien donne une estimation de l’incertitude qui est la variance en chaque point.


\- *"Décrivez les principales fonctions d’acquisition (Expected Improvement, Upper 
Confidence Bound, etc.)." :*
**Réponse :** Une fonction d'acquisition est une fonction qui permettera de choisir les prochains points à tester.
principales fonctions d’acquisition : 
- Expected Improvement  : c'est une fonction qui cherche à maximiser l'amélioration attendue cela signifie qu'elle choisit les points où l’on s'attend à ce que la fonction objective prenne une valeur meilleure que la meilleure valeur observée.
-  Upper Confidence Bound : (probablement la plus simple), elle prend un parametre λ, si celui ci est petit UCB privilégiera les solutions qui devraient être performantes tandis qui si λ est grand, UCB privilégiera l'exploration de zones actuellement inexplorées dans l'espace de recherche.

#### Q4 :
J'ai implementer une optimisation bayesienne en utilisant la fonction gp_minimize de scikit-optimize 'skopt' sur une fonction f.
![](https://github.com/HachimiBouizegarene/ATDN-TP2/blob/master/assets/image.png?raw=true)
