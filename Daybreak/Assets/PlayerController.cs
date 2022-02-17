using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

    Rigidbody2D rigid2D;
    Animator animator;

    const int SIZE = 3;
    float jumpForce = 780.0f;
    float walkSpeed = 0.01f;

    void Start() {
        this.rigid2D = GetComponent<Rigidbody2D>();
        this.animator = GetComponent<Animator>();
    }

    void Update() {

        /* 이동 */
        int key = 0;
        if (Input.GetKey(KeyCode.RightArrow)) {
            key = SIZE;
        }
        if (Input.GetKey(KeyCode.LeftArrow)) {
            key = -SIZE;
        }
        transform.Translate(walkSpeed * key, 0, 0);

        /* 반전 */
        if(key != 0) {     
            transform.localScale = new Vector3(key, SIZE, 1);
        }

        /* 행동 */
        if (Input.GetKeyDown(KeyCode.Space) && this.rigid2D.velocity.y == 0) {
            this.rigid2D.AddForce(transform.up * this.jumpForce);   // 점프
        }
        if (Input.GetKeyDown(KeyCode.A)) {
            this.animator.SetTrigger("Attack1Trigger");             // 공격 1
        }
        if (Input.GetKeyDown(KeyCode.S)) {
            this.animator.SetTrigger("Attack2Trigger");             // 공격 2
        }

        /* 애니메이션 속도 */
        if (this.rigid2D.velocity.y == 0 && key != 0) {
            this.animator.speed = Mathf.Abs(key);                   // 달리기
        } 
        else if (this.rigid2D.velocity.y == 0 && key == 0) {
            this.animator.speed = 1.0f;                             // 걷기
        } 
        else {
            this.animator.speed = 0;                                // 점프
        }
    }

    public void Dead() {
        this.animator.SetTrigger("DeadTrigger");
        Destroy(gameObject, 1);
    }

}
