using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class VeerbewegingFrictie: MonoBehaviour
{	
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
	public int mass;
	public int spring_constant;
	
    // Start is called before the first frame update
    void Start()
    {
        mass = 3;
		transform.position = new Vector3(0,4,0);
		spring_constant = 10;
    }
	
    // Update is called once per frame
    void FixedUpdate()
    {
		Force = -spring_constant * transform.position - Velocity;
		Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
