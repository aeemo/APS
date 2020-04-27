#include<stdio.h> 
#include<stdlib.h> 
   
struct node 
{ 
    int key; 
    struct node *left, *right; 
}; 
   

struct node *newNode(int item) 
{ 
    struct node *temp =  (struct node *)malloc(sizeof(struct node)); 
    temp->key = item; 
    temp->left = temp->right = NULL; 
    return temp; 
} 
   
 
void inorder(struct node *root) 
{ 
    if (root != NULL) 
    { 
        inorder(root->left); 
        printf("%d \n", root->key); 
        inorder(root->right); 
    } 
} 
   

struct node* insert(struct node* node, int key) 
{ 
    
    if (node == NULL) return newNode(key); 
    if (key < node->key) 
        node->left  = insert(node->left, key); 
    else if (key > node->key) 
        node->right = insert(node->right, key);    
    return node; 
} 
   
 
int main() 
{ 
    int r,n=6,i;   
    struct node *root = NULL; 
    printf("Give a root element: ");
    scanf("%d",&r);
    root = insert(root, r); 
    for(i=0;i<6;i++)
    {
    	printf("Give the element: ");
    	scanf("%d",&r);
    	insert(root,r);
	}
    
    inorder(root); 
   
    return 0; 
} 
