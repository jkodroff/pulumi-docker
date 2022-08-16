// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.docker.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.docker.outputs.ContainerMountBindOptions;
import com.pulumi.docker.outputs.ContainerMountTmpfsOptions;
import com.pulumi.docker.outputs.ContainerMountVolumeOptions;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ContainerMount {
    /**
     * @return Optional configuration for the bind type.
     * 
     */
    private final @Nullable ContainerMountBindOptions bindOptions;
    /**
     * @return Whether the mount should be read-only.
     * 
     */
    private final @Nullable Boolean readOnly;
    /**
     * @return Mount source (e.g. a volume name, a host path).
     * 
     */
    private final @Nullable String source;
    /**
     * @return Container path
     * 
     */
    private final String target;
    /**
     * @return Optional configuration for the tmpfs type.
     * 
     */
    private final @Nullable ContainerMountTmpfsOptions tmpfsOptions;
    /**
     * @return The mount type
     * 
     */
    private final String type;
    /**
     * @return Optional configuration for the volume type.
     * 
     */
    private final @Nullable ContainerMountVolumeOptions volumeOptions;

    @CustomType.Constructor
    private ContainerMount(
        @CustomType.Parameter("bindOptions") @Nullable ContainerMountBindOptions bindOptions,
        @CustomType.Parameter("readOnly") @Nullable Boolean readOnly,
        @CustomType.Parameter("source") @Nullable String source,
        @CustomType.Parameter("target") String target,
        @CustomType.Parameter("tmpfsOptions") @Nullable ContainerMountTmpfsOptions tmpfsOptions,
        @CustomType.Parameter("type") String type,
        @CustomType.Parameter("volumeOptions") @Nullable ContainerMountVolumeOptions volumeOptions) {
        this.bindOptions = bindOptions;
        this.readOnly = readOnly;
        this.source = source;
        this.target = target;
        this.tmpfsOptions = tmpfsOptions;
        this.type = type;
        this.volumeOptions = volumeOptions;
    }

    /**
     * @return Optional configuration for the bind type.
     * 
     */
    public Optional<ContainerMountBindOptions> bindOptions() {
        return Optional.ofNullable(this.bindOptions);
    }
    /**
     * @return Whether the mount should be read-only.
     * 
     */
    public Optional<Boolean> readOnly() {
        return Optional.ofNullable(this.readOnly);
    }
    /**
     * @return Mount source (e.g. a volume name, a host path).
     * 
     */
    public Optional<String> source() {
        return Optional.ofNullable(this.source);
    }
    /**
     * @return Container path
     * 
     */
    public String target() {
        return this.target;
    }
    /**
     * @return Optional configuration for the tmpfs type.
     * 
     */
    public Optional<ContainerMountTmpfsOptions> tmpfsOptions() {
        return Optional.ofNullable(this.tmpfsOptions);
    }
    /**
     * @return The mount type
     * 
     */
    public String type() {
        return this.type;
    }
    /**
     * @return Optional configuration for the volume type.
     * 
     */
    public Optional<ContainerMountVolumeOptions> volumeOptions() {
        return Optional.ofNullable(this.volumeOptions);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ContainerMount defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private @Nullable ContainerMountBindOptions bindOptions;
        private @Nullable Boolean readOnly;
        private @Nullable String source;
        private String target;
        private @Nullable ContainerMountTmpfsOptions tmpfsOptions;
        private String type;
        private @Nullable ContainerMountVolumeOptions volumeOptions;

        public Builder() {
    	      // Empty
        }

        public Builder(ContainerMount defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.bindOptions = defaults.bindOptions;
    	      this.readOnly = defaults.readOnly;
    	      this.source = defaults.source;
    	      this.target = defaults.target;
    	      this.tmpfsOptions = defaults.tmpfsOptions;
    	      this.type = defaults.type;
    	      this.volumeOptions = defaults.volumeOptions;
        }

        public Builder bindOptions(@Nullable ContainerMountBindOptions bindOptions) {
            this.bindOptions = bindOptions;
            return this;
        }
        public Builder readOnly(@Nullable Boolean readOnly) {
            this.readOnly = readOnly;
            return this;
        }
        public Builder source(@Nullable String source) {
            this.source = source;
            return this;
        }
        public Builder target(String target) {
            this.target = Objects.requireNonNull(target);
            return this;
        }
        public Builder tmpfsOptions(@Nullable ContainerMountTmpfsOptions tmpfsOptions) {
            this.tmpfsOptions = tmpfsOptions;
            return this;
        }
        public Builder type(String type) {
            this.type = Objects.requireNonNull(type);
            return this;
        }
        public Builder volumeOptions(@Nullable ContainerMountVolumeOptions volumeOptions) {
            this.volumeOptions = volumeOptions;
            return this;
        }        public ContainerMount build() {
            return new ContainerMount(bindOptions, readOnly, source, target, tmpfsOptions, type, volumeOptions);
        }
    }
}
