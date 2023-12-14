import React from 'react';
import styled from 'styled-components';
import amherstLogo from './amherst-logo.png';


const HeaderContainer = styled.div`
  display: flex;
  align-items: center;
  background-color: purple;
  color: white;
  padding: 20px;
  font-size: 24px;
  margin-bottom: 20px;

  img {
    width: 40px; /* Adjust image size as needed */
    margin-right: 10px; /* Add spacing between image and text */
  }

  strong {
    font-weight: bold;
  }
`;

const Header: React.FC = () => {
  return (
    <HeaderContainer>
      <img src={amherstLogo} alt="Logo" />
      <strong>GEO DB</strong>
    </HeaderContainer>
  );
};

export default Header;




