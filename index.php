<?php
// Parametri da inviare
$nome = "Mario";
$età = 25;

// Costruzione della URL con query string
$url = "http://localhost/recezione.py?nome=" . urlencode($nome) . "&età=" . urlencode($età);

// Reindirizzamento alla pagina Python
header("Location: $url");
exit;
?>