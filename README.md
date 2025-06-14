# Implemented-Papers

A comprehensive repository containing implementations of groundbreaking research papers in Machine Learning and Deep Learning. This collection serves as both a learning resource and reference for understanding fundamental concepts through code.

## Repository Structure

```
Implemented-Papers/
├── CNN/
├── NLP/
├── RNN/
├── GAN/
├── Transformers/
├── Computer-Vision/
├── Reinforcement-Learning/
└── Classical-ML/
```

## Computer Vision & CNNs

### Convolutional Neural Networks
- [ ] **LeNet-5** (1998) - *Gradient-based learning applied to document recognition*
- [ ] **AlexNet** (2012) - *ImageNet Classification with Deep Convolutional Neural Networks*
- [ ] **VGGNet** (2014) - *Very Deep Convolutional Networks for Large-Scale Image Recognition*
- [ ] **GoogLeNet/Inception** (2014) - *Going Deeper with Convolutions*
- [ ] **ResNet** (2015) - *Deep Residual Learning for Image Recognition*
- [ ] **DenseNet** (2016) - *Densely Connected Convolutional Networks*
- [ ] **MobileNet** (2017) - *Efficient Convolutional Neural Networks for Mobile Vision Applications*
- [ ] **EfficientNet** (2019) - *Rethinking Model Scaling for Convolutional Neural Networks*

### Object Detection & Segmentation
- [ ] **R-CNN** (2013) - *Rich feature hierarchies for accurate object detection*
- [ ] **Fast R-CNN** (2015) - *Fast Region-based Convolutional Network method*
- [ ] **Faster R-CNN** (2015) - *Towards Real-Time Object Detection with Region Proposal Networks*
- [ ] **YOLO** (2015) - *You Only Look Once: Real-Time Object Detection*
- [ ] **U-Net** (2015) - *Convolutional Networks for Biomedical Image Segmentation*
- [ ] **Mask R-CNN** (2017) - *Instance Segmentation*

## Natural Language Processing

### Foundational NLP Models
- [ ] **Word2Vec** (2013) - *Efficient Estimation of Word Representations in Vector Space*
- [ ] **GloVe** (2014) - *Global Vectors for Word Representation*
- [ ] **Seq2Seq** (2014) - *Sequence to Sequence Learning with Neural Networks*
- [ ] **FastText** (2016) - *Enriching Word Vectors with Subword Information*

### Recurrent Neural Networks
- [ ] **LSTM** (1997) - *Long Short-Term Memory*
- [ ] **GRU** (2014) - *Learning Phrase Representations using RNN Encoder-Decoder*
- [ ] **Bidirectional LSTM** (1997) - *Bidirectional Recurrent Neural Networks*

### Attention & Transformers
- [ ] **Attention is All You Need** (2017) - *The Original Transformer Paper*
- [ ] **BERT** (2018) - *Bidirectional Encoder Representations from Transformers*
- [ ] **GPT** (2018) - *Improving Language Understanding by Generative Pre-Training*
- [ ] **GPT-2** (2019) - *Language Models are Unsupervised Multitask Learners*
- [ ] **T5** (2019) - *Text-to-Text Transfer Transformer*
- [ ] **RoBERTa** (2019) - *Robustly Optimized BERT Pretraining Approach*
- [ ] **ELECTRA** (2020) - *Pre-training Text Encoders as Discriminators Rather Than Generators*

## Generative Models

### Generative Adversarial Networks
- [ ] **GAN** (2014) - *Generative Adversarial Networks*
- [ ] **DCGAN** (2015) - *Deep Convolutional Generative Adversarial Networks*
- [ ] **Pix2Pix** (2016) - *Image-to-Image Translation with Conditional Adversarial Networks*
- [ ] **CycleGAN** (2017) - *Unpaired Image-to-Image Translation*
- [ ] **StyleGAN** (2018) - *A Style-Based Generator Architecture*
- [ ] **BigGAN** (2018) - *Large Scale GAN Training for High Fidelity Natural Image Synthesis*

### Variational Models
- [ ] **VAE** (2013) - *Auto-Encoding Variational Bayes*
- [ ] **β-VAE** (2017) - *Learning Basic Visual Concepts with a Constrained Variational Framework*

## Reinforcement Learning

- [ ] **DQN** (2013) - *Playing Atari with Deep Reinforcement Learning*
- [ ] **Double DQN** (2015) - *Deep Reinforcement Learning with Double Q-learning*
- [ ] **Dueling DQN** (2015) - *Dueling Network Architectures for Deep Reinforcement Learning*
- [ ] **Policy Gradient** (2000) - *Policy Gradient Methods for Reinforcement Learning*
- [ ] **Actor-Critic** (1999) - *Actor-Critic Algorithms*
- [ ] **A3C** (2016) - *Asynchronous Methods for Deep Reinforcement Learning*
- [ ] **PPO** (2017) - *Proximal Policy Optimization Algorithms*
- [ ] **SAC** (2018) - *Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL*

## Classical Machine Learning

- [ ] **Support Vector Machines** (1995) - *Support-Vector Networks*
- [ ] **Random Forest** (2001) - *Random Forests*
- [ ] **AdaBoost** (1997) - *A Decision-Theoretic Generalization of On-Line Learning*
- [ ] **Gradient Boosting** (2001) - *Greedy Function Approximation: A Gradient Boosting Machine*
- [ ] **XGBoost** (2016) - *Scalable Tree Boosting System*
- [ ] **LightGBM** (2017) - *A Highly Efficient Gradient Boosting Decision Tree*

## Implementation Guidelines

### Code Structure
Each implementation should follow this structure:
```
paper_name/
├── README.md          # Paper summary and implementation details
├── model.py          # Core model implementation
├── train.py          # Training script
├── evaluate.py       # Evaluation script
├── data/            # Dataset handling
├── utils/           # Utility functions
└── notebooks/       # Jupyter notebooks with experiments
```

### Requirements
- **Python 3.8+**
- **PyTorch** or **TensorFlow** (depending on implementation)
- **NumPy**, **Pandas**, **Matplotlib**
- Additional libraries as specified in each implementation

## Implementation Status

**Total Papers**: 0/60+  
**Completed**: 0  
**In Progress**: 0  
**Planned**: 60+  

### Progress by Category
- **CNN/Computer Vision**: 0/14
- **NLP**: 0/11
- **Transformers**: 0/7
- **GANs**: 0/8
- **Reinforcement Learning**: 0/8
- **Classical ML**: 0/6

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Implemented-Papers.git
   cd Implemented-Papers
   ```

2. **Navigate to a specific implementation**
   ```bash
   cd CNN/LeNet
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the implementation**
   ```bash
   python train.py
   ```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/new-paper`)
3. **Follow the implementation structure** outlined above
4. **Add comprehensive documentation** in the README
5. **Include proper citations** and references
6. **Test your implementation** thoroughly
7. **Submit a pull request**

## Resources

- [Papers With Code](https://paperswithcode.com/) - Browse state-of-the-art papers
- [arXiv](https://arxiv.org/) - Access research papers
- [Distill](https://distill.pub/) - Clear explanations of ML concepts
- [Towards Data Science](https://towardsdatascience.com/) - ML articles and tutorials

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original paper authors and researchers
- Open source community
- Educational institutions and resources

---

**Note**: This repository is for educational purposes. Please cite original papers when using these implementations in your research or projects.

## Contact

Feel free to reach out for questions, suggestions, or collaborations!

---

*"The best way to understand a paper is to implement it."*
