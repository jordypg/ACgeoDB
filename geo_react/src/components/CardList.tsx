import React from 'react';
import styled from 'styled-components';
import Card from './Card';
import unkownUser from '/home/hwarrich23/ACgeoDB/geo_react/src/Images/unkown_user.jpg';

const CardListContainer = styled.div`
  flex: 3;
  padding: 20px;
  display: flex;
  flex-wrap: wrap;
`;

const cardsData = [
  { name: 'Student 1', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser },
  { name: 'Student 2', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 3', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  // Add more card data as needed
];

const CardList: React.FC = () => {
  return (
    <CardListContainer>
      {cardsData.map((card, index) => (
        <Card key={index} name={card.name} program={card.program} major={card.major} country={card.country} imageUrl={card.imageUrl}/>
      ))}
    </CardListContainer>
  );
};

export default CardList;
