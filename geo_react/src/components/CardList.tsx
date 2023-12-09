import React from 'react';
import styled from 'styled-components';
import Card from './Card';

const CardListContainer = styled.div`
  flex: 3;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
`;

const cardsData = [
  { name: 'Student 1', program: 'Program', major: 'Major', country:'Country' },
  { name: 'Student 2', program: 'Program', major: 'Major', country:'Country'},
  { name: 'Student 3', program: 'Program', major: 'Major', country:'Country'},
  // Add more card data as needed
];

const CardList: React.FC = () => {
  return (
    <CardListContainer>
      {cardsData.map((card, index) => (
        <Card key={index} name={card.name} program={card.program} major={card.major} country={card.country} />
      ))}
    </CardListContainer>
  );
};

export default CardList;
