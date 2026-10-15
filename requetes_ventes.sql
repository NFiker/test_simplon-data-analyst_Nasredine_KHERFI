-- Vérification de l'import
SELECT * FROM ventes;

-- Nombre de lignes
SELECT COUNT(*) AS nombre_lignes FROM ventes;


-- 3.a - Chiffre d'affaires total
SELECT SUM(prix * qte) AS chiffre_affaires_total
FROM ventes;


-- 3.b - Ventes par produit
SELECT 
    produit,
    SUM(qte) AS quantite_vendue,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY produit
ORDER BY produit;


-- 3.c - Ventes par région
SELECT 
    region,
    SUM(qte) AS quantite_vendue,
    SUM(prix * qte) AS chiffre_affaires
FROM ventes
GROUP BY region
ORDER BY region;