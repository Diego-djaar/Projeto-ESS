import styles from "./index.module.css"

function PaginationButtons({ setPage, page, maxPage }) {
    const handlePrevPage = () => {
        setPage(prevPage => prevPage - 1);
    };

    const handleNextPage = () => {
        setPage(prevPage => prevPage + 1);
    };

    return (
        <div className={styles.button}>
            <button onClick={handlePrevPage} disabled={page === 1}>Previous</button>
            <button onClick={handleNextPage} disabled={page === maxPage || maxPage == 0} data-cy="next">Next</button>
        </div>
    );
}

export default PaginationButtons;