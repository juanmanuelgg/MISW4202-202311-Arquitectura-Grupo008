import jwt from "jsonwebtoken";

const SECRET =
  process.env.PROTO_SECRET || "unsecretolargoyporendemuybueno12349876";

function generateJWT(sub, secret = SECRET) {
  const iat = Number(Date.now() / 1000); // es tiempo en segundos
  const payload = {
    sub,
    iat,
    exp: iat + 900, // expira en 15 minutos ... como los de flask
    type: "access",
  };
  return jwt.sign(payload, secret);
}

function verifyJWT(token, secret = SECRET) {
  try {
    const payload = jwt.verify(token, secret);
    return payload;
  } catch {
    return null;
  }
}

export { generateJWT, verifyJWT };
