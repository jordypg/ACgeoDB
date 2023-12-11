// SearchFilter.tsx
import styled from 'styled-components';
import { useFilterContext } from './FilterContext';

const SearchFilterContainer = styled.div`
  margin-bottom: 20px;
`;

const SearchInput = styled.input`
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
`;

const SearchFilter: React.FC = () => {
  const { filterValue, setFilterValue } = useFilterContext();

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFilterValue(event.target.value);
  };


  return (
    <SearchFilterContainer>
      <SearchInput
        type="text"
        placeholder="Search by name, program, or major"
        value={filterValue}
        onChange={handleSearchChange}

      />
    </SearchFilterContainer>
  );
};

export default SearchFilter;
