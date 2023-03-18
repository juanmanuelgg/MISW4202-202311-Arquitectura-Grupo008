import express from "express";
import bodyParser from "body-parser";

import { generateJWT, verifyJWT } from "./jwt-util.js";

const PORT = process.env.PROTO_PORT || 3000;

const app = express();
app.use(bodyParser.json());

app.post("/create-token", (req, res) => {
  const { user, password } = req.body;

  if (user !== "testuser" || password !== "1234567890")
    return res.status(401).send("Usuario o clave incorrectos.");
  else {
    const token = generateJWT({ user });
    return res.status(200).json({ token });
  }
});

app.get("/validate", (req, res) => {
  const ip_cliente = req.headers["x-forwarded-for"] || req.socket.remoteAddress;

  if (!req.headers.authorization)
    return res.status(401).json({ error: "No envió token." });

  const token = req.headers.authorization;
  if (!token.startsWith("Bearer "))
    return res.status(401).json({ error: "Formato de token invalido." });

  const payload = verifyJWT(token.slice("Bearer ".length));
  if (!payload) return res.status(401).send(`Token invalido (${ip_cliente}).`);
  else return res.status(200).send(`Token valido (${ip_cliente}).`);
});

app.listen(PORT, () => {
  console.log(
    `Autenticador proto-token ejecutandose en el puerto ${PORT} (http://localhost:${PORT})`
  );
});
