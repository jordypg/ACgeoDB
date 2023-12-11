import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Card from './Card';
import { useFilterContext } from './FilterContext';
import unkownUser from '/home/jyoon23/ACgeoDB/geo_react/src/Images/unkown_user.jpg';

interface OriginalData {
  country: string;
  majors: string[];
  pgr_id: number;
  program: string;
  random_name: string;
  student_email: string;
}

interface TransformedData {
  key:number;
  name: string;
  program: string;
  major: string;
  country: string;
  imageUrl: string;
  pgr_id: number;
}

const CardListContainer = styled.div`
flex: 3;
padding: 20px;
display: flex;
flex-wrap: wrap;
max-height: 800px; /* Set the maximum height as needed */
overflow-y: auto; /* Add vertical scrollbar if content overflows */
`;


const CardList: React.FC = () => {
  const [cardsData, setCardsData] = useState<TransformedData[]>([]);
  // Assuming your Flask server is running on http://localhost:5000
const apiUrl = 'http://localhost:5000/get_all_cards';

// Function to fetch data from the Flask API
useEffect(() => {
  const fetchData = async () => {
    try {
      const response = await fetch(apiUrl);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data: OriginalData[] = await response.json();

      const transformedData: TransformedData[] = data.map(item => {
        const joinedMajors = item.majors.filter(major => major !== '').join(', ');
        return {
          key:1,
          pgr_id: item.pgr_id,
          name: item.random_name,
          program: item.program,
          major: joinedMajors,
          country: item.country,
          imageUrl: unkownUser,
        };
      });

      setCardsData(transformedData);
    } catch (error: any) {
      console.error('Error fetching data:', error.message);
    }
  };
  fetchData();
}, []);

const fetchCardDetails = async (pgrId: number) => {
  const detailsUrl = `http://localhost:5000/get_backside?pgr_id=${pgrId}}`; // Replace with the actual URL
  try {
    const response = await fetch(detailsUrl);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const cardDetails = await response.json();
    // Process and use cardDetails as needed
  } catch (error: any) {
    console.error('Error fetching card details:', error.message);
  }
};

const onCardClick = async (pgrId: number) => {
  try {
    const cardDetails = await fetchCardDetails(pgrId);
    // Use cardDetails here as needed, e.g., updating state, showing in modal, etc.
  } catch (error) {
    // Handle any errors that occurred during fetchCardDetails
  }
};



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
        <Card key={index} name={card.name} program={card.program} major={card.major} country={card.country} imageUrl={card.imageUrl} onCardClick={() => onCardClick(card.pgr_id)}
        />
      ))}
    </CardListContainer>
  );
};

export default CardList;
