import React from 'react';
import styled from 'styled-components';
import { CardBacksideDetails } from './CardList'; // Adjust the path as needed

// Define the props for the Modal component
interface ModalProps {
  show: boolean;
  onClose: () => void;
  cardBacksideDetails: CardBacksideDetails | null;
}

// Styled component for the modal
const ModalContainer = styled.div`
  position: fixed;
  z-index: 1000; // Ensure it's above other elements
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4); // Semi-transparent background
  // Other styles you might want to include
  padding: 20px;
  box-sizing: border-box;
`;

const ModalContent = styled.div`
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
`;

const CloseButton = styled.span`
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;

  &:hover,
  &:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
`;

// Modal component
// const Modal: React.FC<ModalProps> = ({ show, onClose, cardBacksideDetails }) => {
//   console.log("Modal received backside details:", cardBacksideDetails);

//   return (
//     <ModalContainer show={show}>
//       <ModalContent>
//         <CloseButton onClick={onClose}>&times;</CloseButton>
//         {/* Render card backside details here */}
//         {cardBacksideDetails && (
//           <div>
//             {/* Example rendering of details */}
//             <p>{'sex'}</p>
//             <p>{cardBacksideDetails.academic_exc_comments}</p>
//             {/* Add more fields as needed */}
//           </div>
//         )}
//       </ModalContent>
//     </ModalContainer>
//   );
// };

const Modal: React.FC<ModalProps> = ({ show, onClose, cardBacksideDetails }) => {
  if (!show){
    return null
  }
  return (
    <ModalContainer style={{ display: show ? 'block' : 'none' }}>
      <ModalContent>
        <CloseButton onClick={onClose}>&times;</CloseButton>
        {cardBacksideDetails ? (
          <div>
            <p><strong>Academic Comments:</strong> {cardBacksideDetails.academic_exc_comments}</p>
            <p><strong>Rating:</strong> {cardBacksideDetails.academic_exc_rating}</p>
            <p><strong>Amount Spent:</strong> {cardBacksideDetails.amount_spent}</p>
            <p><strong>Attitudes Different:</strong> {cardBacksideDetails.attitudes_diff}</p>
            <p><strong>Attitudes Different Comments:</strong> {cardBacksideDetails.attitudes_diff_comments}</p>
            <p><strong>Challenges:</strong> {cardBacksideDetails.challenges}</p>
            <p><strong>City Affordability:</strong> {cardBacksideDetails.city_affordability}</p>
            <p><strong>Courses Taken:</strong> {cardBacksideDetails.courses_taken}</p>
            <p><strong>Growth:</strong> {cardBacksideDetails.growth}</p>
            <p><strong>Housing Accomodations:</strong> {cardBacksideDetails.housing_acc}</p>
            <p><strong>Housing Accomodations Comments:</strong> {cardBacksideDetails.housing_acc_comments}</p>
            <p><strong>Leisure Excursion Rating:</strong> {cardBacksideDetails.leisure_exc_rating}</p>
            <p><strong>Leisure Excursion Comments:</strong> {cardBacksideDetails.leisure_exc_comments}</p>
            <p><strong>New Perspectives:</strong> {cardBacksideDetails.new_perspectives}</p>
            <p><strong>Primary Reason:</strong> {cardBacksideDetails.primary_reason}</p>
            <p><strong>Term ID:</strong> {cardBacksideDetails.term_id}</p>
            {/* Render other fields similarly */}
          </div>
        ) : (
          <p>Loading details...</p>
        )}
      </ModalContent>
    </ModalContainer>
  );
};

export default Modal;
