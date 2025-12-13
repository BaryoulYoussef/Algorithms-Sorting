# Sorting Algorithm 

This project compare the performance of five different sorting algorithms: Heap Sort, Merge Sort, Quick Sort, Radix Sort, and Shell Sort.

##  Features

- **Multiple Sorting Algorithms**: Heap Sort, Merge Sort, Quick Sort, Radix Sort, Shell Sort
- **Performance Metrics**: Precise execution time measurements
- **Interactive Visualizations**: Dynamic charts comparing algorithm performance
- **User-Friendly Interface**: Built with Streamlit for seamless interaction

## 📚 Inspiration

This work is inspired by the research paper:

**"Comparative Analysis of the Performance of Popular Sorting Algorithms on Datasets of Different Sizes and Characteristics"**

**Authors:**
- Ahmed S. Sabah
- Samy S. Abu-Naser
- Yasmeen Emad Helles
- Ruba Fikri Abdallatif
- Faten Y.A. Abu Samra
- Aya Helmi Abu Taha
- Nawal Maher Massa
- Ahmed A. Hamouda

📄 [Read the Paper](paper.pdf)

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
```

### Installation

1. Clone the repository

```bash
git clone https://github.com/BaryoulYoussef/Algorithms-Sorting.git
cd SORTING-ALGORIITHMS
```


### Usage



1. **Run the web application**
```bash
streamlit run app.py
```

3. **Upload your CSV file** and select a numeric column to benchmark

4. **View results** and download the performance report

## 📁 Project Structure

```
sorting-benchmark-tool/
├── All_Sorting_Methods.py    # Sorting algorithm implementations
├── Experiments.py             # Benchmarking class
├── app.py                     # Streamlit web interface
└── README.md                  # Project documentation
```

## 🛠️ Algorithms Implemented

| Algorithm | Time Complexity (Average) | Space Complexity | Stable |
|-----------|---------------------------|------------------|--------|
| Heap Sort | O(n log n) | O(1) | No |
| Merge Sort | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(log n) | No |
| Radix Sort | O(nk) | O(n + k) | Yes |
| Shell Sort | O(n log² n) | O(1) | No |

## 📊 Example Output

The tool provides:
- Ranked performance table
- Execution time in seconds
- Winner announcement
- Interactive bar chart visualization
- Downloadable CSV results

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 👤 Author

**[Youssef Baryoul]**

- GitHub: [@Youssef Baryoul](https://github.com/BaryoulYoussef)
- LinkedIn: [Youssef Baryoul](https://www.linkedin.com/in/youssef-baryoul/E)


## 🙏 Acknowledgments

- Special thanks to the authors of the research paper for their comprehensive analysis
- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)

---

⭐ Star this repository if you find it helpful!