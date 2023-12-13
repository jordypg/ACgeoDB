import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Card from './Card';
import { useFilterContext } from './FilterContext';
import unkownUser from '/home/jyoon23/ACgeoDB/geo_react/src/Images/unkown_user.jpg';
import Modal from './Modal'

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

export interface CardBacksideDetails {
  academic_exc_comments: string,
  academic_exc_rating: string,
  amount_spent: string,
  attitudes_diff: string,
  attitudes_diff_comments: string,
  challenges: string,
  city_affordability: string,  
  courses_taken: string,
  growth: string,
  housing_acc: string,
  housing_acc_comments: string,
  leisure_exc_comments: string, 
  leisure_exc_rating: string,
  new_perspectives: string, 
  primary_reason: string,
  term_id: string
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
  const [selectedCardBackside, setSelectedCardBackside] = useState<CardBacksideDetails | null>(null);
  const [showModal, setShowModal] = useState(false);

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
          key: 1,
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
  const detailsUrl = `http://127.0.0.1:5000//get_backside?pgr_id=${pgrId}`; // Replace with the actual URL
  try {
    const response = await fetch(detailsUrl);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const cardDetails = await response.json();
    if (Array.isArray(cardDetails) && cardDetails.length > 0) {
      // setSelectedCardBackside(cardDetails[0]);
      return cardDetails[0]; // Return the first element of the array
      
    } else {
      return null; // Return null if the array is empty or not an array
    }
    // console.log("Fetched details:", cardDetails); // Log the fetched detailsfetfet
    // setSelectedCardBackside(cardDetails);
    // return cardDetails; // Return the fetched details
    // Process and use cardDetails as needed
  } catch (error: any) {
    console.error('Error fetching card details:', error.message);
  }
};

const onCardClick = async (pgrId: number) => {
  try {
    const cardDetails = await fetchCardDetails(pgrId);
    if (cardDetails) {
      setSelectedCardBackside(cardDetails); // Update the state with the fetched details
      console.log("Selected card backside details:", cardDetails); // Log to check
      setShowModal(true); // Show the modal
    }
    // Use cardDetails here as needed, e.g., updating state, showing in modal, etc.
  } catch (error) {
    console.error('Error:', error);
  }
};

const handleCloseModal = () => {
  setShowModal(false);
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

<Modal
        show={showModal}
        onClose={handleCloseModal}
        cardBacksideDetails={selectedCardBackside}
      />
    </CardListContainer>
  );
};

export default CardList;
