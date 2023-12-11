import React, { useEffect, useState } from 'react';
import styled from 'styled-components';
import Card from './Card';
import Modal from './Modal';
import { useFilterContext } from './FilterContext';
import unkownUser from '/home/hwarrich23/ACgeoDB/geo_react/src/Images/unkown_user.jpg';

interface OriginalData {
  country: string;
  majors: string[];
  pgr_id: string;
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
  onCardClick: () => void;
}
interface CardProps {
  key: number;
  name: string;
  program: string;
  major: string;
  country: string;
  imageUrl: string;
  onCardClick: () => void;
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
          name: item.random_name,
          program: item.program,
          major: joinedMajors,
          country: item.country,
          imageUrl: unkownUser,
          onCardClick: () => null// Replace with actual image URL if available
        };
      });

      setCardsData(transformedData);
    } catch (error: any) {
      console.error('Error fetching data:', error.message);
    }
  };
  fetchData();
}, []);

  const { filterValue } = useFilterContext();
  const filteredCards = cardsData.filter((card) =>
    card.name.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.program.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.major.toLowerCase().includes(filterValue.toLowerCase()) ||
    card.country.toLowerCase().includes(filterValue.toLowerCase())
  );

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedCard, setSelectedCard] = useState<CardProps | null>(null);
  const openModal = (card: CardProps) => {
    setSelectedCard(card);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setSelectedCard(null);
    setIsModalOpen(false);
  };
  return (
    <CardListContainer>
      {filteredCards.map((card, index) => (
        <Card key={index} name={card.name} program={card.program} major={card.major} country={card.country} imageUrl={card.imageUrl} onCardClick={() => openModal(card)}/>
      ))}
      <Modal
        isOpen={isModalOpen}
        onClose={closeModal}
        content={selectedCard ? `Modal Content for ${selectedCard.name}` : null}
      />
    </CardListContainer>
  );
};

export default CardList;
