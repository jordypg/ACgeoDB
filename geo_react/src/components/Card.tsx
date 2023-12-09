import React from 'react';
import styled from 'styled-components';

interface CardProps {
  key: number;
  name: string;
  program: string;
  major: string;
  country: string;
}

const CardContainer = styled.div`
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin: 10px;
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;

  &:hover {
    transform: scale(1.05);
  }
`;

const CardTitle = styled.h3`
  color: #333;
  font-size: 18px;
  margin-bottom: 10px;
`;

const CardContent = styled.p`
  color: #666;
  font-size: 14px;
  margin-bottom: 20px; /* Adjust the margin as needed */
`;

const Card: React.FC<CardProps> = ({name, program, major, country}) => {
    return (
      <CardContainer>
        <CardTitle>{name}</CardTitle>
        <CardContent>{program}</CardContent>
        <CardContent>{major}</CardContent>
        <CardContent>{country}</CardContent>
      </CardContainer>
    );
  };

export default Card;
