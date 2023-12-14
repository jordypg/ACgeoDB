import React from 'react';
import styled from 'styled-components';

interface CardProps {
  key: number;
  // pgr_id: number;
  name: string;
  program: string;
  major: string;
  country: string;
  imageUrl: string;
  onCardClick: () => void;
}

const CardContainer = styled.div`
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: 300px; /* Fixed width */
  height: auto; /* Auto height */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  &:hover {
    transform: scale(1.05);
  }
  display: flex;
`;

const CardContentContainer = styled.div`
  flex: 1;
`;

const ImageContainer = styled.div`
  width: 180px;
  height: 150px;
  margin-left: 10px;
  margin-top: 13px;
  border-radius: 8px;
  overflow: hidden;
`;

const CardImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;
`;

const CardTitle = styled.h3`
  color: #333;
  font-size: 18px;
  margin-bottom: 10px;
`;

const CardContent = styled.p`
  color: #666;
  font-size: 14px;
  margin-bottom: 20px;
`;

const Card: React.FC<CardProps> = ({ name, program, major, country, imageUrl, onCardClick }) => {
  return (
    <CardContainer onClick={onCardClick}> 
      <CardContentContainer>
        <CardTitle>{name}</CardTitle>
        <CardContent>{program}</CardContent>
        <CardContent>{major}</CardContent>
        <CardContent>{country}</CardContent>
      </CardContentContainer>
      <ImageContainer>
        <CardImage src={imageUrl} alt={`${name}'s image`} />
      </ImageContainer>
    </CardContainer>
  );
};

export default Card;
