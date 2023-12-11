import React from 'react';
import styled from 'styled-components';
import Card from './Card';
import { useFilterContext } from './FilterContext';
import unkownUser from '/home/hwarrich23/ACgeoDB/geo_react/src/Images/unkown_user.jpg';


const CardListContainer = styled.div`
flex: 3;
padding: 20px;
display: flex;
flex-wrap: wrap;
max-height: 800px; /* Set the maximum height as needed */
overflow-y: auto; /* Add vertical scrollbar if content overflows */
`;

const cardsData = [
  { name: 'Student 1', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser },
  { name: 'Student 2', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 3', program: 'Program', major: 'Chem', country:'Country', imageUrl:unkownUser},
  { name: 'Student 4', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 5', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 6', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 7', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 8', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 9', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 10', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 11', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 12', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 13', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 14', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 15', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 16', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 17', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  { name: 'Student 18', program: 'Program', major: 'Major', country:'Country', imageUrl:unkownUser},
  // Add more card data as needed
];


const CardList: React.FC = () => {
  const { filterValue } = useFilterContext();
  const filteredCards = cardsData.filter((card) =>
    card.name.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.program.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.major.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.country.toLowerCase().includes(filterValue.toLowerCase())
  );
  return (
    <CardListContainer>
      {filteredCards.map((card, index) => (
        <Card key={index} name={card.name} program={card.program} major={card.major} country={card.country} imageUrl={card.imageUrl}/>
      ))}
    </CardListContainer>
  );
};

export default CardList;
