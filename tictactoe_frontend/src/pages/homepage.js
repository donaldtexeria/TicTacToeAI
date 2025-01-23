import React from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Tic Tac Toe!</h1>
      <p>Select a mode:</p>
      <button onClick={() => navigate("/game?mode=human-vs-human")}>
        Human vs Human
      </button>
      <button onClick={() => navigate("/game?mode=human-vs-ai")}>
        Human vs AI
      </button>
    </div>
  );
};

export default HomePage;
