import React, { createContext, useContext, useState, ReactNode } from 'react';

interface ModalContextProps {
  isOpen: boolean;
  content: React.ReactNode;
  openModal: (content: React.ReactNode) => void;
  closeModal: () => void;
}

const ModalContext = createContext<ModalContextProps | undefined>(undefined);

export const ModalProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [content, setContent] = useState<React.ReactNode | null>(null);

  const openModal = (modalContent: React.ReactNode) => {
    setContent(modalContent);
    setIsOpen(true);
  };

  const closeModal = () => {
    setContent(null);
    setIsOpen(false);
  };

  return (
    <ModalContext.Provider value={{ isOpen, content, openModal, closeModal }}>
      {children}
    </ModalContext.Provider>
  );
};

export const useModalContext = () => {
  const context = useContext(ModalContext);
  if (!context) {
    throw new Error('useModalContext must be used within a ModalProvider');
  }
  return context;
};
