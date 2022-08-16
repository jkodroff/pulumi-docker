// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class ServiceTaskSpecContainerSpecLabel {
    /**
     * @return Name of the label
     * 
     */
    private final String label;
    /**
     * @return Value of the label
     * 
     */
    private final String value;

    @CustomType.Constructor
    private ServiceTaskSpecContainerSpecLabel(
        @CustomType.Parameter("label") String label,
        @CustomType.Parameter("value") String value) {
        this.label = label;
        this.value = value;
    }

    /**
     * @return Name of the label
     * 
     */
    public String label() {
        return this.label;
    }
    /**
     * @return Value of the label
     * 
     */
    public String value() {
        return this.value;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ServiceTaskSpecContainerSpecLabel defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private String label;
        private String value;

        public Builder() {
    	      // Empty
        }

        public Builder(ServiceTaskSpecContainerSpecLabel defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.label = defaults.label;
    	      this.value = defaults.value;
        }

        public Builder label(String label) {
            this.label = Objects.requireNonNull(label);
            return this;
        }
        public Builder value(String value) {
            this.value = Objects.requireNonNull(value);
            return this;
        }        public ServiceTaskSpecContainerSpecLabel build() {
            return new ServiceTaskSpecContainerSpecLabel(label, value);
        }
    }
}
