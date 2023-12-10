// SearchFilter.tsx
import React, { useState } from 'react';
import styled from 'styled-components';

interface SearchFilterProps {
  onSearch: (query: string) => void;
}

const SearchFilterContainer = styled.div`
  margin-bottom: 20px;
`;

const SearchInput = styled.input`
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
`;

const SearchFilter: React.FC<SearchFilterProps> = ({ onSearch }) => {
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchQuery(event.target.value);
    onSearch(searchQuery);
  };


  return (
    <SearchFilterContainer>
      <SearchInput
        type="text"
        placeholder="Search by name, program, or major"
        value={searchQuery}
        onChange={handleSearchChange}
      />
    </SearchFilterContainer>
  );
};

export default SearchFilter;
