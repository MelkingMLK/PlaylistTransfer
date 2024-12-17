<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casella di Testo Accattivante</title>
    <!-- Stile CSS -->
    <style>
        /* Stile generale della pagina */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #6dd5ed, #2193b0);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #fff;
        }

        /* Contenitore principale */
        .container {
            background: #ffffff;
            color: #333;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 30px;
            text-align: center;
            width: 90%;
            max-width: 400px;
            animation: fadeIn 1s ease-in-out;
        }

        /* Titolo della pagina */
        h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #2193b0;
        }

        /* Stile per la casella di testo */
        textarea {
            width: 100%;
            height: 120px;
            border: 2px solid #2193b0;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
            resize: none;
        }

        /* Effetto focus sulla casella di testo */
        textarea:focus {
            border-color: #6dd5ed;
            box-shadow: 0 0 10px rgba(109, 213, 237, 0.5);
        }

        /* Pulsante di invio */
        button {
            margin-top: 15px;
            background: #6dd5ed;
            border: none;
            color: #fff;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.3s ease;
        }

        button:hover {
            background: #2193b0;
        }

        /* Animazione di fade-in */
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <!-- Contenitore principale -->
    <div class="container">
        <h1>Inserisci il tuo testo</h1>
        <form method="POST" action="">
            <!-- Casella di testo -->
            <textarea name="user_text" placeholder="Scrivi qualcosa qui..."></textarea>
            <br>
            <!-- Pulsante di invio -->
            <button type="submit">Invia</button>
        </form>
        <!-- Stampa il contenuto inviato -->
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST["user_text"])) {
            $user_text = htmlspecialchars($_POST["user_text"]);
            echo "<p><strong>Hai scritto:</strong></p>";
            echo "<p style='color: #2193b0; word-wrap: break-word;'>$user_text</p>";
        }
        ?>
    </div>
</body>
</html>