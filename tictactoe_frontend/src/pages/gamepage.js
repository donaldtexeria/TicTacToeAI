import React from "react";
import { useNavigate, useSearchParams } from "react-router-dom";
import GameBoard from "../components/gameboard";

const GamePage = () => {
  const navigate = useNavigate();
  const [searchparams] = useSearchParams();
  const mode = searchparams.get("mode");

  return (
    <div>
      <h1>Tic Tac Toe!</h1>
      <p>
        Mode: {mode === "human-vs-human" ? "Human vs Human" : "Human vs Ai"}
      </p>
      <GameBoard />
      <h1>TO BE IMPLEMENTED</h1>
    </div>
  );
};

export default GamePage;
