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
const ModalContainer = styled.div<{ show: boolean }>`
  display: ${({ show }) => (show ? 'block' : 'none')};
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
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
    <ModalContainer show>
      <ModalContent>
        <CloseButton onClick={onClose}>&times;</CloseButton>
        {cardBacksideDetails ? (
          <div>
            <p>Academic Comments: {cardBacksideDetails.academic_exc_comments}</p>
            <p>Rating: {cardBacksideDetails.academic_exc_rating}</p>
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
