import styled from 'styled-components';

interface CardProps {
  key: number;
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
  width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  width: '300px';
  height: '200px'
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out, width 0.3s ease-in-out, height 0.3s ease-in-out;
  &:hover {
    transform: scale(1.05);
  }
  display: flex;
`;

const CardContentContainer = styled.div`
  flex: 1;
`;

const ImageContainer = styled.div`
  width: 180px; /* Adjust the width of the image container */
  height: 150px; /* Adjust the height of the image container */
  margin-left: 10 px; /* Adjust the margin as needed */
  overflow: hidden;
  margin-top: 13px;
  border-radius: 8px; /* Optional: Add border-radius for a rounded image container */
`;

const CardImage = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover; /* Ensure the image covers the container */
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

const Card: React.FC<CardProps> = ({name, program, major, country, imageUrl,  onCardClick }) => {
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
