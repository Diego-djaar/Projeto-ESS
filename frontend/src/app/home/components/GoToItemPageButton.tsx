import React from 'react';
import { Link } from 'react-router-dom';
import homeIcon from '../assets/homeIcon.png'
import './GoToitemPageButton.css'

const GoToItemPageButton: React.FC = () => {
  return (
    <Link to="/itempage" className="itemPageButton">
      <img src={homeIcon} alt="Home" />
    </Link>
  );
};

export default GoToItemPageButton;
