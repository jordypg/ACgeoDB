import React from 'react';
import styled from 'styled-components';

const HeaderContainer = styled.div`
  background-color: purple;
  color: white;
  padding: 20px;
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
`;

const Header: React.FC = () => {
  return <HeaderContainer>GEO DB</HeaderContainer>;
};

export default Header;
