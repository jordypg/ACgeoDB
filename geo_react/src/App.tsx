import styled from 'styled-components';
import Header from './components/Header';
import FilterSection from './components/FilterSection';
import CardList from './components/CardList';

const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh; /* Use the full height of the viewport */
`;

const ContentContainer = styled.div`
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  height: 100%; /* Use the full height of the container */
`;

const App: React.FC = () => {

  return (
    <AppContainer>
      <Header />
      <ContentContainer>
        <FilterSection/>
        <CardList/>
      </ContentContainer>
    </AppContainer>
  );
};

export default App;
